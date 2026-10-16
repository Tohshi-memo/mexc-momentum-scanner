# Decision Report

- generated_at: 2026-10-16T01:31:19.954183+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16780**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16780, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.65% | **-0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.77% | **+0.73%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_BB3S | 5/12 | 41.7% | +0.94% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.82% | **+1.91%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.93% | **+1.57%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.40% | **+1.36%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.18% | **+1.09%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.50% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$121.36** / 初期 $100.00 (+21.36%)
- 確定トレード: 241件 (TP 89 / SL 145 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,260.96** / 初期 $100.00 (+1160.96%)
- 確定: 6314件 (Win 1849 / Loss 2026 / Flat 2439) / skip 7027件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STBL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,260.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.98** / 初期 $100.00 (+175.98%)
- 確定: 3675件 (Win 1024 / Loss 871 / Flat 1780) / skip 6516件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0457 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STBL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $275.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4941件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000235 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-16T01:31:07.992633+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=82171.0
- Funnel: target 1090 → liquid 188 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +53.40% | $6,610,444.99 |
| STBL/USDT:USDT | +35.22% | $1,200,315.07 |
| SI/USDT:USDT | +21.43% | $2,147,602.42 |
| RIVER/USDT:USDT | +10.99% | $4,129,694.88 |
| CT/USDT:USDT | +10.36% | $1,190,864.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SI/USDT:USDT | below_1h_threshold | +2.76% | +2.92% |
| INJ/USDT:USDT | below_1h_threshold | +1.23% | +1.38% |
| 1000RATS/USDT:USDT | below_1h_threshold | +1.04% | +1.20% |
| AGT/USDT:USDT | below_1h_threshold | +1.01% | +1.17% |
| AKE/USDT:USDT | below_1h_threshold | +0.87% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
