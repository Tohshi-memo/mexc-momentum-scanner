# Decision Report

- generated_at: 2026-08-24T00:16:22.963866+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12480**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12480, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.45% | **-0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.98% | **+0.78%** |
| LIMIT_BB3S | 7/16 | 43.8% | +0.81% | **+0.36%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.76% | **+2.07%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +2.60% | **+1.69%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.76% | **+1.38%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +2.07% | **+0.72%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.10% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$710.92** / 初期 $100.00 (+610.92%)
- 確定: 4507件 (Win 1375 / Loss 1475 / Flat 1657) / skip 4534件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZORA/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $710.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.26** / 初期 $100.00 (+57.26%)
- 確定: 1956件 (Win 536 / Loss 469 / Flat 951) / skip 3935件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0037 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZORA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $157.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.75** / 初期 $100.00 (+16.75%)
- 確定: 1872件 (Win 551 / Loss 708 / Flat 613) / pending 3件 / skip 2081件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000091 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $116.75

## 6. Latest Market Context

- 更新: 2026-08-24T00:16:14.067561+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=77584.7
- Funnel: target 1018 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SPK/USDT:USDT | +14.37% | $6,743,814.42 |
| GRASS/USDT:USDT | +12.79% | $2,396,827.78 |
| BASECAT/USDT:USDT | +10.21% | $2,947,778.39 |
| LIT/USDT:USDT | +8.92% | $9,351,071.72 |
| TUT/USDT:USDT | +8.81% | $53,520,723.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TOKYOELSTOCK/USDT:USDT | below_1h_threshold | +1.74% | +1.90% |
| SPK/USDT:USDT | below_1h_threshold | +1.42% | +1.58% |
| NEAR/USDT:USDT | below_1h_threshold | +1.29% | +1.45% |
| 1000RATS/USDT:USDT | below_1h_threshold | +0.79% | +0.95% |
| CYS/USDT:USDT | below_1h_threshold | +0.77% | +0.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
