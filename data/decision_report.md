# Decision Report

- generated_at: 2026-06-03T19:54:15.150203+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5576**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5576, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.71% | **-0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +3.67% | **+1.10%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.52% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/12 | 41.7% | +5.07% | **+2.11%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.03% | **+1.82%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.18% | **+1.64%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.24% | **+1.35%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$97.09** / 初期 $100.00 (-2.91%)
- 確定トレード: 92件 (TP 27 / SL 62 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.09
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1004件 (Win 239 / Loss 312 / Flat 453) / skip 1133件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-03T19:54:12.270257+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.86% price=65434.9
- Funnel: target 768 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +51.30% | $12,928,079.51 |
| STO/USDT:USDT | +47.55% | $3,746,825.29 |
| BP/USDT:USDT | +11.60% | $1,470,605.38 |
| RAVE/USDT:USDT | +9.16% | $2,475,773.12 |
| BEAT/USDT:USDT | +7.62% | $7,182,776.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +4.87% | +5.73% |
| BEAT/USDT:USDT | below_1h_threshold | +4.53% | +5.39% |
| HOME/USDT:USDT | below_1h_threshold | +4.31% | +5.17% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.98% | +2.84% |
| EPIC/USDT:USDT | below_1h_threshold | +1.59% | +2.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
