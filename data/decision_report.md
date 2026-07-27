# Decision Report

- generated_at: 2026-07-27T23:11:13.360803+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9657**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9657, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.49% | **-2.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +7.15% | **+1.07%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_BB3S | 7/15 | 46.7% | +1.64% | **+0.76%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.62% | **+0.16%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.24% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.74% | **+1.74%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +5.73% | **+1.15%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.56% | **+1.02%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +2.30% | **+0.92%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.84% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$105.86** / 初期 $100.00 (+5.86%)
- 確定トレード: 147件 (TP 50 / SL 92 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $105.86
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$461.56** / 初期 $100.00 (+361.56%)
- 確定: 3435件 (Win 1088 / Loss 1118 / Flat 1229) / skip 2783件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COTI/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $461.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1224件 (Win 338 / Loss 275 / Flat 611) / skip 1844件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0451 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.79** / 初期 $100.00 (+8.79%)
- 確定: 677件 (Win 221 / Loss 256 / Flat 200) / pending 3件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000175 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.79

## 6. Latest Market Context

- 更新: 2026-07-27T23:11:08.478318+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=63614.1
- Funnel: target 902 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +51.39% | $5,889,626.81 |
| JIMOTHY/USDT:USDT | +22.06% | $1,695,363.35 |
| SOONNETWORK/USDT:USDT | +10.64% | $1,221,050.71 |
| KAITO/USDT:USDT | +8.66% | $7,951,067.43 |
| AEON1/USDT:USDT | +8.00% | $1,841,458.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DEXE/USDT:USDT | below_1h_threshold | +2.40% | +2.62% |
| BANK/USDT:USDT | below_1h_threshold | +2.36% | +2.58% |
| RIF/USDT:USDT | below_1h_threshold | +0.90% | +1.13% |
| ON/USDT:USDT | below_1h_threshold | +0.90% | +1.12% |
| CAP/USDT:USDT | below_1h_threshold | +0.74% | +0.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
