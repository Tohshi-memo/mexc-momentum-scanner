# Decision Report

- generated_at: 2026-08-21T22:11:31.351695+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12265**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12265, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.00% | **-0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/17 | 52.9% | +4.02% | **+2.13%** |
| LIMIT_7PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_6PCT | 5/20 | 25.0% | +5.55% | **+1.39%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.30% | **+1.38%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.16% | **+0.97%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.25% | **+0.88%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.82% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$659.02** / 初期 $100.00 (+559.02%)
- 確定: 4385件 (Win 1342 / Loss 1438 / Flat 1605) / skip 4441件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.90% 残高後 $659.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.84** / 初期 $100.00 (+54.84%)
- 確定: 1872件 (Win 515 / Loss 448 / Flat 909) / skip 3804件
- 成長率目線: 平均log +0.000234 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1013 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $154.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1914件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000241 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T22:11:20.683808+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=78566.4
- Funnel: target 1018 → liquid 216 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +187.62% | $2,720,375.85 |
| CATE/USDT:USDT | +35.77% | $10,586,380.51 |
| JIMOTHY/USDT:USDT | +31.79% | $1,551,662.83 |
| NIULAI/USDT:USDT | +13.63% | $2,738,052.43 |
| STX/USDT:USDT | +12.79% | $1,656,481.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLOKI/USDT:USDT | below_1h_threshold | +3.97% | +3.87% |
| KAITO/USDT:USDT | below_1h_threshold | +3.27% | +3.18% |
| GALA/USDT:USDT | below_1h_threshold | +2.25% | +2.15% |
| STX/USDT:USDT | below_1h_threshold | +2.06% | +1.96% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.74% | +1.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
