# Decision Report

- generated_at: 2026-08-03T23:01:22.812166+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10254**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10254, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.78% | **-0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.77% | **+0.46%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.58% | **+0.06%** |
| LIMIT_BB3S | 5/17 | 29.4% | -0.19% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.72% | **+1.03%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.92% | **+0.96%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.43% | **+0.64%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$590.53** / 初期 $100.00 (+490.53%)
- 確定: 3712件 (Win 1176 / Loss 1214 / Flat 1322) / skip 3103件
- 成長率目線: 平均log +0.000478 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KORU/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $590.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2382件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0575 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.71** / 初期 $100.00 (+16.71%)
- 確定: 1029件 (Win 331 / Loss 398 / Flat 300) / pending 6件 / skip 694件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000517 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KORU/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $116.71

## 6. Latest Market Context

- 更新: 2026-08-03T23:01:15.520571+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=63545.5
- Funnel: target 929 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIPPIN/USDT:USDT | +14.98% | $5,977,084.63 |
| PLTRSTOCK/USDT:USDT | +14.61% | $3,246,902.23 |
| KOMA/USDT:USDT | +11.62% | $2,230,655.57 |
| KORU/USDT:USDT | +11.08% | $16,731,834.40 |
| SNXX/USDT:USDT | +9.06% | $7,564,771.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLTRSTOCK/USDT:USDT | below_1h_threshold | +2.01% | +2.08% |
| KORU/USDT:USDT | below_1h_threshold | +1.47% | +1.54% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.10% | +1.17% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.08% | +1.15% |
| MUU/USDT:USDT | below_1h_threshold | +1.07% | +1.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
