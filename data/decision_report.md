# Decision Report

- generated_at: 2026-06-05T10:40:04.829630+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5712**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.58% / filled 20/20。**
- 全期間 MARKET基準: n=5712, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.07% | **+0.91%** |
| ASK | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.89% | **+0.71%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.84% | **+0.64%** |
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.82% | **+0.53%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.24% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1010件 (Win 239 / Loss 313 / Flat 458) / skip 1263件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-05T10:40:01.587954+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.75% price=62363.2
- Funnel: target 773 → liquid 161 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +80.65% | $23,316,109.67 |
| BABY/USDT:USDT | +57.06% | $5,300,057.27 |
| CLO/USDT:USDT | +20.29% | $1,108,167.51 |
| OPN/USDT:USDT | +14.78% | $40,689,154.73 |
| BEAT/USDT:USDT | +11.77% | $28,372,709.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APPSTOCK/USDT:USDT | below_1h_threshold | +2.66% | +3.41% |
| AVGOSTOCK/USDT:USDT | below_1h_threshold | +0.43% | +1.18% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +0.41% | +1.15% |
| LMTSTOCK/USDT:USDT | below_1h_threshold | +0.40% | +1.15% |
| BTW/USDT:USDT | below_1h_threshold | +0.32% | +1.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
