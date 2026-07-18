# Decision Report

- generated_at: 2026-07-18T18:46:11.897141+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8968**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8968, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-3.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.02% | **-3.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 12/20 | 60.0% | +1.89% | **+1.13%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.94% | **+0.78%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.60% | **+0.64%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.16% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.70% | **+3.33%** |
| MARKET_LONG | 20/20 | 100.0% | +2.80% | **+2.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.90% | **+2.73%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +5.44% | **+2.72%** |
| LIMIT_4PCT_LONG | 5/20 | 25.0% | +4.07% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$110.69** / 初期 $100.00 (+10.69%)
- 確定トレード: 116件 (TP 43 / SL 69 / EXP 4)
- 最新: B/USDT:USDT SL_HIT PnL -3.30% 残高後 $110.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$358.77** / 初期 $100.00 (+258.77%)
- 確定: 3049件 (Win 946 / Loss 973 / Flat 1130) / skip 2480件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $358.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$117.28** / 初期 $100.00 (+17.28%)
- 確定: 929件 (Win 229 / Loss 188 / Flat 512) / skip 1450件
- 成長率目線: 平均log +0.000172 / 幾何平均 +0.017% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1258 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RAVE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $117.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.04** / 初期 $100.00 (-0.96%)
- 確定: 196件 (Win 62 / Loss 107 / Flat 27) / pending 0件 / skip 242件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000459 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAVE/USDT:USDT `MARKET` EXPIRED account +0.16% 残高後 $99.04

## 6. Latest Market Context

- 更新: 2026-07-18T18:46:05.100903+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64455.5
- Funnel: target 885 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +65.16% | $20,956,223.47 |
| BANK/USDT:USDT | +39.10% | $17,529,404.93 |
| B/USDT:USDT | +15.12% | $27,641,912.97 |
| US/USDT:USDT | +6.07% | $4,561,188.58 |
| TAG/USDT:USDT | +6.06% | $1,362,960.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +4.02% | +4.01% |
| TAG/USDT:USDT | below_1h_threshold | +4.00% | +3.99% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.55% | +3.54% |
| AKE/USDT:USDT | below_1h_threshold | +2.51% | +2.50% |
| RAVE/USDT:USDT | below_1h_threshold | +1.65% | +1.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
