# Decision Report

- generated_at: 2026-08-23T03:56:16.536930+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12439**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12439, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.44% | **-0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +0.90% | **+0.63%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.14% | **+0.63%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.93% | **+0.58%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.05% | **+1.44%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.68% | **+1.18%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.55% | **+0.93%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$706.12** / 初期 $100.00 (+606.12%)
- 確定: 4466件 (Win 1367 / Loss 1460 / Flat 1639) / skip 4534件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $706.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1935件 (Win 533 / Loss 465 / Flat 937) / skip 3915件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0007 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.84** / 初期 $100.00 (+16.84%)
- 確定: 1863件 (Win 549 / Loss 706 / Flat 608) / pending 0件 / skip 2049件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000116 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.84

## 6. Latest Market Context

- 更新: 2026-08-23T03:56:09.938092+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=76961.6
- Funnel: target 1018 → liquid 207 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +50.79% | $48,622,953.80 |
| ZRO/USDT:USDT | +11.92% | $11,192,682.53 |
| UAI/USDT:USDT | +10.24% | $3,377,882.76 |
| STX/USDT:USDT | +7.80% | $10,653,821.68 |
| CHIP/USDT:USDT | +7.79% | $2,016,204.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGI/USDT:USDT | below_1h_threshold | +4.20% | +4.35% |
| TUT/USDT:USDT | below_1h_threshold | +2.84% | +3.00% |
| HEMI/USDT:USDT | below_1h_threshold | +2.39% | +2.55% |
| TOKYOELSTOCK/USDT:USDT | below_1h_threshold | +1.96% | +2.12% |
| ROBO/USDT:USDT | below_1h_threshold | +1.20% | +1.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
