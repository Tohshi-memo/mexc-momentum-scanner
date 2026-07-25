# Decision Report

- generated_at: 2026-07-25T08:26:23.567127+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9501**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9501, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.12% | **-2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.50% | **+0.52%** |
| LIMIT_6PCT | 3/20 | 15.0% | +2.85% | **+0.43%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.22% | **+0.08%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.15% | **+0.01%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.38% | **-0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.75% | **+2.62%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.84% | **+1.92%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.95% | **+1.66%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.10% | **+1.24%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.46% | **+1.23%** |

## 2. $100 Live Portfolio

- 残高: **$103.79** / 初期 $100.00 (+3.79%)
- 確定トレード: 139件 (TP 46 / SL 88 / EXP 5)
- 最新: SYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.79
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$433.56** / 初期 $100.00 (+333.56%)
- 確定: 3331件 (Win 1052 / Loss 1078 / Flat 1201) / skip 2731件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $433.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1165件 (Win 312 / Loss 254 / Flat 599) / skip 1747件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1300 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$106.33** / 初期 $100.00 (+6.33%)
- 確定: 549件 (Win 185 / Loss 211 / Flat 153) / pending 4件 / skip 420件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000427 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $106.33

## 6. Latest Market Context

- 更新: 2026-07-25T08:26:13.389393+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=63944.1
- Funnel: target 897 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DEXE/USDT:USDT | +109.46% | $79,534,288.01 |
| EUL/USDT:USDT | +34.50% | $3,317,229.91 |
| AKE/USDT:USDT | +28.40% | $47,106,421.81 |
| PROM/USDT:USDT | +22.75% | $3,014,112.67 |
| B2/USDT:USDT | +18.54% | $3,214,026.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +1.63% | +1.68% |
| SYN/USDT:USDT | below_1h_threshold | +1.34% | +1.39% |
| RIF/USDT:USDT | below_1h_threshold | +1.22% | +1.26% |
| B2/USDT:USDT | below_1h_threshold | +1.15% | +1.20% |
| AKE/USDT:USDT | below_1h_threshold | +1.01% | +1.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
