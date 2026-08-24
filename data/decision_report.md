# Decision Report

- generated_at: 2026-08-24T13:16:20.398199+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12515**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12515, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/15 | 26.7% | +2.58% | **+0.69%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.62% | **+0.43%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.87% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.69% | **+1.53%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.92% | **+1.25%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.74% | **+1.13%** |
| MARKET_LONG | 20/20 | 100.0% | +0.97% | **+0.97%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.24% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$703.82** / 初期 $100.00 (+603.82%)
- 確定: 4510件 (Win 1375 / Loss 1477 / Flat 1658) / skip 4566件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $703.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.71** / 初期 $100.00 (+56.71%)
- 確定: 1972件 (Win 536 / Loss 470 / Flat 966) / skip 3954件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0127 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.03** / 初期 $100.00 (+16.03%)
- 確定: 1898件 (Win 557 / Loss 718 / Flat 623) / pending 3件 / skip 2084件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000237 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SUPER/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.03

## 6. Latest Market Context

- 更新: 2026-08-24T13:16:11.417893+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=79062.1
- Funnel: target 1019 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +57.33% | $1,394,349.30 |
| CASHCAT/USDT:USDT | +35.99% | $1,258,929.19 |
| PROM/USDT:USDT | +27.14% | $13,101,150.75 |
| SUPER/USDT:USDT | +25.46% | $1,908,491.92 |
| PORTAL/USDT:USDT | +22.89% | $4,148,192.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FF/USDT:USDT | below_1h_threshold | +1.84% | +1.94% |
| BTR/USDT:USDT | below_1h_threshold | +1.68% | +1.79% |
| TUT/USDT:USDT | below_1h_threshold | +1.54% | +1.64% |
| BASECAT/USDT:USDT | below_1h_threshold | +1.44% | +1.54% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.44% | +1.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
