# Decision Report

- generated_at: 2026-07-16T10:26:20.886284+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8799**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8799, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.00% | **-0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.27% | **+0.15%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.14% | **+0.10%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| MARKET | 20/20 | 100.0% | -0.00% | **-0.00%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.40% | **+1.12%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.59% | **+1.03%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.34% | **+0.80%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.06% | **+0.64%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.75% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$106.87** / 初期 $100.00 (+6.87%)
- 確定トレード: 104件 (TP 38 / SL 64 / EXP 2)
- 最新: ROAM/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.87
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$337.15** / 初期 $100.00 (+237.15%)
- 確定: 2914件 (Win 908 / Loss 945 / Flat 1061) / skip 2446件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $337.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.20** / 初期 $100.00 (+7.20%)
- 確定: 761件 (Win 174 / Loss 169 / Flat 418) / skip 1449件
- 成長率目線: 平均log +0.000091 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0084 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $107.20

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.30** / 初期 $100.00 (-1.70%)
- 確定: 71件 (Win 21 / Loss 46 / Flat 4) / pending 2件 / skip 198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000462 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.30

## 6. Latest Market Context

- 更新: 2026-07-16T10:26:14.883397+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=64168.1
- Funnel: target 875 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +18.41% | $5,942,123.51 |
| US/USDT:USDT | +18.06% | $16,035,569.50 |
| BANK/USDT:USDT | +15.17% | $2,684,298.26 |
| AKE/USDT:USDT | +14.27% | $43,902,256.32 |
| CAP/USDT:USDT | +14.16% | $2,907,740.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNHSTOCK/USDT:USDT | below_1h_threshold | +4.77% | +4.61% |
| BANK/USDT:USDT | below_1h_threshold | +3.33% | +3.17% |
| VELVET/USDT:USDT | below_1h_threshold | +2.19% | +2.03% |
| ENJ/USDT:USDT | below_1h_threshold | +1.51% | +1.35% |
| ORDI/USDT:USDT | below_1h_threshold | +1.42% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
