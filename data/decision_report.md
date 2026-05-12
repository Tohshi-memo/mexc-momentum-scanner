# Decision Report

- generated_at: 2026-05-12T15:33:04.760334+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4139**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=4139, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.06% | **+1.06%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.64% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.19% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.53** / 初期 $100.00 (+17.53%)
- 確定: 275件 (Win 77 / Loss 95 / Flat 103) / skip 425件
- 成長率目線: 平均log +0.000587 / 幾何平均 +0.059% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRUTH/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $117.53

## 4. Latest Market Context

- 更新: 2026-05-12T15:33:00.842055+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=80335.7
- Funnel: target 763 → liquid 197 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.7 >= 65=1, 4h RSI 86.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +99.08% | $33,090,844.88 |
| GIGA/USDT:USDT | +51.35% | $7,985,057.82 |
| SKYAI/USDT:USDT | +40.94% | $40,013,832.32 |
| GUA/USDT:USDT | +36.29% | $3,958,558.30 |
| USELESS/USDT:USDT | +33.84% | $11,483,070.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOLV/USDT:USDT | below_1h_threshold | +4.49% | +4.71% |
| DYM/USDT:USDT | below_1h_threshold | +3.63% | +3.85% |
| BASED/USDT:USDT | below_1h_threshold | +3.01% | +3.23% |
| H/USDT:USDT | below_1h_threshold | +2.91% | +3.13% |
| RIF/USDT:USDT | below_1h_threshold | +1.99% | +2.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
