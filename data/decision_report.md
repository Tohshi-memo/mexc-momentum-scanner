# Decision Report

- generated_at: 2026-06-15T09:58:21.018657+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6770**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6770, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.80% | **+0.28%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.00% | **-0.00%** |
| LIMIT_BB3S | 6/17 | 35.3% | -0.03% | **-0.01%** |
| LIMIT_5PCT | 10/20 | 50.0% | -0.04% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.20% | **+1.65%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.04% | **+1.52%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.84% | **+1.47%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RIF/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.02
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$177.15** / 初期 $100.00 (+77.15%)
- 確定: 1643件 (Win 429 / Loss 507 / Flat 707) / skip 1688件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $177.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.28** / 初期 $100.00 (-0.72%)
- 確定: 137件 (Win 27 / Loss 22 / Flat 88) / skip 44件
- 成長率目線: 平均log -0.000053 / 幾何平均 -0.005% per trade / maxDD +2.07%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_robust_growth_score) / robust_score +0.0043 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +0.69% 残高後 $99.28

## 5. Latest Market Context

- 更新: 2026-06-15T09:58:13.680315+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=65562.5
- Funnel: target 770 → liquid 143 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.6 >= 65=1, 4h RSI 67.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +90.59% | $26,772,516.90 |
| ASTEROID/USDT:USDT | +83.04% | $4,515,881.23 |
| CLO/USDT:USDT | +45.32% | $2,306,603.32 |
| H/USDT:USDT | +42.31% | $142,672,899.77 |
| PUFFER/USDT:USDT | +35.79% | $1,293,865.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PUFFER/USDT:USDT | below_1h_threshold | +4.56% | +4.65% |
| XPL/USDT:USDT | below_1h_threshold | +2.99% | +3.08% |
| NIL/USDT:USDT | below_1h_threshold | +1.90% | +1.99% |
| MEGA/USDT:USDT | below_1h_threshold | +1.57% | +1.66% |
| EVAA/USDT:USDT | below_1h_threshold | +1.53% | +1.62% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
