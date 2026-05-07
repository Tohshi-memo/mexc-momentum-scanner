# Decision Report

- generated_at: 2026-05-07T16:42:51.257159+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3662**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3662, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.50% | **-1.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +2.36% | **+1.18%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.44% | **+0.39%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.48% | **+1.91%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.57% | **+1.80%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.90% | **+1.76%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.73% | **+1.49%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.28% | **+1.31%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$112.16** / 初期 $100.00 (+12.16%)
- 確定: 156件 (Win 46 / Loss 53 / Flat 57) / skip 67件
- 成長率目線: 平均log +0.000735 / 幾何平均 +0.074% per trade / maxDD +2.62%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JTO/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $112.16

## 4. Latest Market Context

- 更新: 2026-05-07T16:42:42.471857+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=79820.0
- Funnel: target 771 → liquid 181 → pre 50 → checked 50 → surge 7 → strict 5
- Surge前reject: below_1h_threshold=43, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.9 >= 65=1, 4h RSI 77.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +42.00% | $4,600,760.86 |
| HIGH/USDT:USDT | +11.37% | $1,240,573.69 |
| B/USDT:USDT | +9.75% | $3,918,866.03 |
| FHE/USDT:USDT | +8.73% | $14,146,525.07 |
| LAB/USDT:USDT | +8.12% | $270,178,920.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| M/USDT:USDT | below_1h_threshold | +4.25% | +4.30% |
| JTO/USDT:USDT | below_1h_threshold | +4.03% | +4.09% |
| NOT/USDT:USDT | below_1h_threshold | +3.58% | +3.63% |
| AVNT/USDT:USDT | below_1h_threshold | +3.18% | +3.23% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +3.01% | +3.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
