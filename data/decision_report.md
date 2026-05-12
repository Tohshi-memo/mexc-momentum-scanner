# Decision Report

- generated_at: 2026-05-12T14:53:10.832833+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4132**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.23% / filled 20/20。**
- 全期間 MARKET基準: n=4132, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.09% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.14% | **+0.74%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.33% | **+0.18%** |
| MARKET_LONG | 20/20 | 100.0% | +0.15% | **+0.15%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |
| ASK_LONG | 20/20 | 100.0% | -0.02% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.08** / 初期 $100.00 (+17.08%)
- 確定: 268件 (Win 74 / Loss 92 / Flat 102) / skip 425件
- 成長率目線: 平均log +0.000588 / 幾何平均 +0.059% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $117.08

## 4. Latest Market Context

- 更新: 2026-05-12T14:53:07.132396+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=80523.1
- Funnel: target 763 → liquid 197 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +77.18% | $29,006,344.99 |
| GIGA/USDT:USDT | +57.59% | $7,648,381.64 |
| SKYAI/USDT:USDT | +41.17% | $40,360,121.96 |
| GUA/USDT:USDT | +34.69% | $3,761,030.16 |
| USELESS/USDT:USDT | +33.10% | $11,161,630.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +3.42% | +3.30% |
| PENGUIN/USDT:USDT | below_1h_threshold | +2.67% | +2.56% |
| B/USDT:USDT | below_1h_threshold | +2.49% | +2.38% |
| CYS/USDT:USDT | below_1h_threshold | +1.83% | +1.72% |
| TWT/USDT:USDT | below_1h_threshold | +1.60% | +1.49% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
