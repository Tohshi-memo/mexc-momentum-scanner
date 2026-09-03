# Decision Report

- generated_at: 2026-09-03T16:21:47.280241+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13505**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13505, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.45% | **-1.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.12% | **-0.03%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +3.59% | **+2.33%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +4.11% | **+2.06%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.49% | **+1.92%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.43% | **+1.82%** |
| MARKET_LONG | 20/20 | 100.0% | +0.85% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5008件 (Win 1516 / Loss 1644 / Flat 1848) / skip 5058件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BONER/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.36% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2373件 (Win 671 / Loss 576 / Flat 1126) / skip 4543件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2059 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.09** / 初期 $100.00 (+17.09%)
- 確定: 2186件 (Win 653 / Loss 855 / Flat 678) / pending 4件 / skip 2792件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000643 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BONER/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.09

## 6. Latest Market Context

- 更新: 2026-09-03T16:21:30.792845+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.65% price=80787.2
- Funnel: target 1046 → liquid 163 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +9.77% | $2,354,375.86 |
| BULLA/USDT:USDT | +9.68% | $10,257,126.06 |
| FONE/USDT:USDT | +7.10% | $1,093,179.42 |
| APR/USDT:USDT | +4.56% | $1,312,909.69 |
| PROM/USDT:USDT | +4.11% | $4,530,952.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_1h_threshold | +4.72% | +5.37% |
| PROM/USDT:USDT | below_1h_threshold | +4.12% | +4.77% |
| ENA/USDT:USDT | below_1h_threshold | +2.51% | +3.16% |
| KORU/USDT:USDT | below_1h_threshold | +2.12% | +2.77% |
| GPROSTOCK/USDT:USDT | below_1h_threshold | +2.04% | +2.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
