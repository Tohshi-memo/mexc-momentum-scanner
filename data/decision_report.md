# Decision Report

- generated_at: 2026-08-02T03:21:35.476726+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10140**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10140, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.37% | **-1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.78% | **+0.67%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 7/18 | 38.9% | +1.29% | **+0.50%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.69% | **+2.01%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.66% | **+1.73%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$586.16** / 初期 $100.00 (+486.16%)
- 確定: 3659件 (Win 1165 / Loss 1196 / Flat 1298) / skip 3042件
- 成長率目線: 平均log +0.000483 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $586.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1280件 (Win 359 / Loss 297 / Flat 624) / skip 2271件
- 成長率目線: 平均log +0.000267 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1180 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$113.42** / 初期 $100.00 (+13.42%)
- 確定: 948件 (Win 303 / Loss 368 / Flat 277) / pending 6件 / skip 659件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000474 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $113.42

## 6. Latest Market Context

- 更新: 2026-08-02T03:21:19.442082+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63411.1
- Funnel: target 922 → liquid 129 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 1000RATS/USDT:USDT | +58.63% | $25,188,469.81 |
| BLESS/USDT:USDT | +36.59% | $7,259,887.61 |
| UAI/USDT:USDT | +29.90% | $19,748,441.22 |
| GIGGLE/USDT:USDT | +14.41% | $19,152,629.92 |
| PUMPFUN/USDT:USDT | +6.65% | $18,460,288.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +4.80% | +4.82% |
| SATS/USDT:USDT | below_1h_threshold | +3.23% | +3.25% |
| KORU/USDT:USDT | below_1h_threshold | +3.10% | +3.12% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.64% | +2.66% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.48% | +2.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
