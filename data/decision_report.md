# Decision Report

- generated_at: 2026-06-15T08:28:25.357803+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6764**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6764, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.31% | **-1.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.80% | **+0.28%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.00% | **-0.00%** |
| LIMIT_BB3S | 4/17 | 23.5% | -0.12% | **-0.03%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.15% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.58% | **+2.58%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.18% | **+1.85%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.12% | **+1.72%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.34% | **+1.52%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.84% | **+1.34%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RIF/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.02
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$177.58** / 初期 $100.00 (+77.58%)
- 確定: 1637件 (Win 428 / Loss 505 / Flat 704) / skip 1688件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $177.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.95** / 初期 $100.00 (-1.05%)
- 確定: 131件 (Win 26 / Loss 21 / Flat 84) / skip 44件
- 成長率目線: 平均log -0.000081 / 幾何平均 -0.008% per trade / maxDD +2.07%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_robust_growth_score) / robust_score -0.0021 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $98.95

## 5. Latest Market Context

- 更新: 2026-06-15T08:28:20.850290+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=65663.4
- Funnel: target 770 → liquid 143 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +87.76% | $4,002,686.52 |
| EVAA/USDT:USDT | +87.65% | $24,548,935.80 |
| CLO/USDT:USDT | +43.09% | $2,191,502.14 |
| PUFFER/USDT:USDT | +32.32% | $1,089,277.54 |
| TRADOOR/USDT:USDT | +29.15% | $4,293,329.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.53% | +4.50% |
| EVAA/USDT:USDT | below_1h_threshold | +4.12% | +4.09% |
| PUFFER/USDT:USDT | below_1h_threshold | +3.47% | +3.44% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.55% | +2.52% |
| AAVE/USDT:USDT | below_1h_threshold | +2.28% | +2.25% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
