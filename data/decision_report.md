# Decision Report

- generated_at: 2026-09-05T18:16:20.968292+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13769**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13769, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.59% | **-0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.50% | **+0.35%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.23% | **+0.31%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.71% | **+0.35%** |
| MARKET_LONG | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.56% | **+0.25%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +0.19% | **+0.08%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.01** / 初期 $100.00 (+759.01%)
- 確定: 5075件 (Win 1522 / Loss 1654 / Flat 1899) / skip 5255件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UNI/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $859.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.32** / 初期 $100.00 (+88.32%)
- 確定: 2514件 (Win 700 / Loss 593 / Flat 1221) / skip 4666件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0546 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $188.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.74** / 初期 $100.00 (+19.74%)
- 確定: 2386件 (Win 708 / Loss 905 / Flat 773) / pending 2件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000280 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.74

## 6. Latest Market Context

- 更新: 2026-09-05T18:16:07.991469+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=79950.1
- Funnel: target 1050 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +20.95% | $2,240,992.23 |
| 4/USDT:USDT | +20.68% | $24,900,318.59 |
| BASECAT/USDT:USDT | +13.56% | $2,062,293.87 |
| NIULAI/USDT:USDT | +11.77% | $2,727,800.31 |
| USELESS/USDT:USDT | +10.44% | $20,543,614.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASECAT/USDT:USDT | below_1h_threshold | +2.54% | +2.64% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.16% | +2.26% |
| UNI/USDT:USDT | below_1h_threshold | +2.03% | +2.13% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.56% | +1.66% |
| ARB/USDT:USDT | below_1h_threshold | +0.93% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
