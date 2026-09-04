# Decision Report

- generated_at: 2026-09-04T22:11:12.945655+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13672**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13672, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.28% | **+0.18%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.21% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.95% | **+1.95%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.16% | **+1.62%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.43% | **+1.58%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.48% | **+0.74%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +0.91% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 201件 (TP 75 / SL 121 / EXP 5)
- 最新: UAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5011件 (Win 1516 / Loss 1644 / Flat 1851) / skip 5222件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.38** / 初期 $100.00 (+85.38%)
- 確定: 2424件 (Win 682 / Loss 577 / Flat 1165) / skip 4659件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0412 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.36** / 初期 $100.00 (+18.36%)
- 確定: 2308件 (Win 687 / Loss 884 / Flat 737) / pending 3件 / skip 2834件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000317 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $118.36

## 6. Latest Market Context

- 更新: 2026-09-04T22:11:03.280123+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=79616.0
- Funnel: target 1050 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +44.41% | $7,831,776.32 |
| BASECAT/USDT:USDT | +30.76% | $1,957,776.13 |
| MARSCOIN/USDT:USDT | +13.11% | $8,434,327.05 |
| USELESS/USDT:USDT | +11.21% | $44,055,780.90 |
| DASH/USDT:USDT | +10.77% | $21,817,455.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASECAT/USDT:USDT | below_1h_threshold | +2.78% | +2.74% |
| 4/USDT:USDT | below_1h_threshold | +1.89% | +1.85% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.59% | +1.55% |
| BTR/USDT:USDT | below_1h_threshold | +1.43% | +1.39% |
| TUT/USDT:USDT | below_1h_threshold | +1.11% | +1.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
