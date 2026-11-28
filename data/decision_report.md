# Decision Report

- generated_at: 2026-11-28T08:46:27.283225+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19829**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19829, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.06% | **-0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +2.57% | **+1.29%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.67% | **+1.00%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.85% | **+0.74%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.94% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.10% | **+1.24%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.29% | **+0.97%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.18% | **+0.94%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$122.01** / 初期 $100.00 (+22.01%)
- 確定トレード: 293件 (TP 107 / SL 176 / EXP 10)
- 最新: EVAA/USDT:USDT TP_HIT PnL +8.00% 残高後 $122.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,950.51** / 初期 $100.00 (+1850.51%)
- 確定: 7656件 (Win 2203 / Loss 2465 / Flat 2988) / skip 8734件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAG/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $1,950.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$460.06** / 初期 $100.00 (+360.06%)
- 確定: 5298件 (Win 1410 / Loss 1141 / Flat 2747) / skip 7942件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0487 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $460.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7991件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000132 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-28T08:46:13.256849+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=59584.8
- Funnel: target 1101 → liquid 138 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +62.82% | $1,184,015.63 |
| EVAA/USDT:USDT | +41.57% | $27,629,529.75 |
| BTW/USDT:USDT | +29.08% | $13,990,419.83 |
| ACE/USDT:USDT | +10.50% | $3,953,461.62 |
| SKY/USDT:USDT | +8.52% | $4,168,459.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.83% | +5.19% |
| BTW/USDT:USDT | below_1h_threshold | +1.60% | +1.97% |
| NIGHT/USDT:USDT | below_1h_threshold | +1.25% | +1.61% |
| SNXX/USDT:USDT | below_1h_threshold | +0.57% | +0.94% |
| MUU/USDT:USDT | below_1h_threshold | +0.56% | +0.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
