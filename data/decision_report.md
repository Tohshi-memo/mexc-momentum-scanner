# Decision Report

- generated_at: 2026-07-02T17:45:09.548298+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8096**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8096, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.98% | **-1.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.22% | **+0.52%** |
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +3.82% | **+2.86%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.76% | **+2.07%** |
| MARKET_LONG | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.83% | **+1.72%** |
| ASK_LONG | 20/20 | 100.0% | +1.02% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$103.14** / 初期 $100.00 (+3.14%)
- 確定トレード: 52件 (TP 19 / SL 32 / EXP 1)
- 最新: TAIKO/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.14
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2213件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 557件 (Win 136 / Loss 131 / Flat 290) / skip 950件
- 成長率目線: 平均log +0.000090 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0321 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T17:45:00.488807+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=61745.1
- Funnel: target 834 → liquid 173 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +11.31% | $2,331,567.50 |
| ALLO/USDT:USDT | +9.94% | $16,586,385.66 |
| BASED/USDT:USDT | +9.72% | $14,301,624.25 |
| O/USDT:USDT | +7.78% | $3,163,241.49 |
| TAIKO/USDT:USDT | +4.73% | $101,637,721.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.96% | +4.80% |
| ALLO/USDT:USDT | below_1h_threshold | +4.95% | +4.79% |
| RIF/USDT:USDT | below_1h_threshold | +3.53% | +3.37% |
| EVAA/USDT:USDT | below_1h_threshold | +3.31% | +3.15% |
| LIT/USDT:USDT | below_1h_threshold | +2.50% | +2.34% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
