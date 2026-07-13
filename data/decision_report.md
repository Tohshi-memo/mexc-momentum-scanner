# Decision Report

- generated_at: 2026-07-13T16:56:20.177121+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8643**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8643, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.37% | **+0.30%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1618 | 5/20 | 25.0% | +0.85% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.13% | **+1.17%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.90% | **+1.14%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.21% | **+0.88%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.96% | **+0.82%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$101.19** / 初期 $100.00 (+1.19%)
- 確定トレード: 94件 (TP 31 / SL 61 / EXP 2)
- 最新: AIOT/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$327.32** / 初期 $100.00 (+227.32%)
- 確定: 2811件 (Win 884 / Loss 923 / Flat 1004) / skip 2393件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $327.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.11** / 初期 $100.00 (+5.11%)
- 確定: 645件 (Win 152 / Loss 159 / Flat 334) / skip 1409件
- 成長率目線: 平均log +0.000077 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0128 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $105.11

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.48** / 初期 $100.00 (-0.52%)
- 確定: 39件 (Win 14 / Loss 25 / Flat 0) / pending 0件 / skip 75件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000320 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $99.48

## 6. Latest Market Context

- 更新: 2026-07-13T16:56:13.696298+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.55% price=62252.9
- Funnel: target 867 → liquid 162 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +10.12% | $20,568,508.54 |
| AIOT/USDT:USDT | +9.12% | $2,044,837.34 |
| ALLO/USDT:USDT | +3.90% | $18,772,887.17 |
| ANSEM/USDT:USDT | +3.24% | $4,532,063.21 |
| USELESS/USDT:USDT | +2.36% | $1,312,632.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +3.88% | +4.43% |
| ANSEM/USDT:USDT | below_1h_threshold | +3.25% | +3.80% |
| USELESS/USDT:USDT | below_1h_threshold | +2.38% | +2.93% |
| BILL/USDT:USDT | below_1h_threshold | +2.20% | +2.75% |
| UNI/USDT:USDT | below_1h_threshold | +1.51% | +2.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
