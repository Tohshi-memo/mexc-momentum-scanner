# Decision Report

- generated_at: 2026-09-04T21:56:27.367661+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13671**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13671, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.58% | **-0.58%** |

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
| MARKET_LONG | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.87% | **+1.40%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.01% | **+1.31%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.80% | **+0.54%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +0.49% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 201件 (TP 75 / SL 121 / EXP 5)
- 最新: UAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5011件 (Win 1516 / Loss 1644 / Flat 1851) / skip 5221件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.38** / 初期 $100.00 (+85.38%)
- 確定: 2424件 (Win 682 / Loss 577 / Flat 1165) / skip 4658件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0503 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.36** / 初期 $100.00 (+18.36%)
- 確定: 2307件 (Win 687 / Loss 884 / Flat 736) / pending 4件 / skip 2834件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000309 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $118.36

## 6. Latest Market Context

- 更新: 2026-09-04T21:56:14.147327+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=79539.3
- Funnel: target 1050 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +38.24% | $7,576,623.27 |
| BASECAT/USDT:USDT | +27.96% | $2,121,205.62 |
| MARSCOIN/USDT:USDT | +12.95% | $8,506,690.46 |
| DASH/USDT:USDT | +12.08% | $21,427,139.63 |
| USELESS/USDT:USDT | +11.91% | $44,450,080.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASECAT/USDT:USDT | below_1h_threshold | +3.31% | +3.45% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.24% | +3.39% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.65% | +2.79% |
| DASH/USDT:USDT | below_1h_threshold | +2.48% | +2.63% |
| USELESS/USDT:USDT | below_1h_threshold | +1.33% | +1.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
