# Decision Report

- generated_at: 2026-07-28T20:11:11.075153+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9725**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9725, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.62% | **-0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_BB3S | 12/18 | 66.7% | +1.24% | **+0.82%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.64% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.08% | **+1.98%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.57% | **+1.02%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.30% | **+0.99%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.05% | **+0.53%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +1.38% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定トレード: 150件 (TP 52 / SL 93 / EXP 5)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.44
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$499.20** / 初期 $100.00 (+399.20%)
- 確定: 3495件 (Win 1106 / Loss 1134 / Flat 1255) / skip 2791件
- 成長率目線: 平均log +0.000460 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $499.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1910件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1239 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.12** / 初期 $100.00 (+10.12%)
- 確定: 743件 (Win 241 / Loss 283 / Flat 219) / pending 4件 / skip 450件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000460 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $110.12

## 6. Latest Market Context

- 更新: 2026-07-28T20:11:04.126217+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=63900.6
- Funnel: target 904 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +31.65% | $1,357,669.39 |
| BTW/USDT:USDT | +16.36% | $5,730,209.57 |
| RIF/USDT:USDT | +14.95% | $4,554,142.68 |
| ON/USDT:USDT | +14.36% | $35,873,857.40 |
| BEAT/USDT:USDT | +10.64% | $58,675,737.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.21% | +1.19% |
| TAO/USDT:USDT | below_1h_threshold | +1.15% | +1.12% |
| BEAT/USDT:USDT | below_1h_threshold | +1.08% | +1.05% |
| ACH/USDT:USDT | below_1h_threshold | +0.70% | +0.67% |
| CELHSTOCK/USDT:USDT | below_1h_threshold | +0.51% | +0.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
