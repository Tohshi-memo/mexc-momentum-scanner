# Decision Report

- generated_at: 2026-08-05T05:01:25.699418+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10364**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10364, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.04% | **+0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| MARKET | 20/20 | 100.0% | +0.04% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +2.97% | **+2.54%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.06% | **+1.96%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.69% | **+1.27%** |
| MARKET_LONG | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.23% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$607.71** / 初期 $100.00 (+507.71%)
- 確定: 3760件 (Win 1192 / Loss 1230 / Flat 1338) / skip 3165件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRVT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $607.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.22** / 初期 $100.00 (+42.22%)
- 確定: 1299件 (Win 365 / Loss 303 / Flat 631) / skip 2476件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1089 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GRVT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $142.22

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.60** / 初期 $100.00 (+18.60%)
- 確定: 1115件 (Win 359 / Loss 430 / Flat 326) / pending 4件 / skip 719件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000403 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRVT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.60

## 6. Latest Market Context

- 更新: 2026-08-05T05:01:15.339511+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64131.5
- Funnel: target 939 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +90.20% | $10,172,025.02 |
| HFT/USDT:USDT | +42.35% | $1,198,282.60 |
| BLESS/USDT:USDT | +40.35% | $22,578,067.07 |
| TAKE/USDT:USDT | +35.55% | $1,576,200.71 |
| CASHCAT/USDT:USDT | +35.27% | $1,191,168.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +2.20% | +2.22% |
| MVLL/USDT:USDT | below_1h_threshold | +1.89% | +1.91% |
| GRVT/USDT:USDT | below_1h_threshold | +1.41% | +1.43% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.08% | +1.09% |
| HFT/USDT:USDT | below_1h_threshold | +0.98% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
