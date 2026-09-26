# Decision Report

- generated_at: 2026-09-26T17:36:55.615629+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15610**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15610, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.03% | **+0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.11% | **+0.44%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| MARKET | 20/20 | 100.0% | +0.03% | **+0.03%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.10% | **+1.47%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.23% | **+1.04%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.42% | **+0.92%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.42% | **+0.85%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.53% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,277.46** / 初期 $100.00 (+1177.46%)
- 確定: 5971件 (Win 1766 / Loss 1917 / Flat 2288) / skip 6200件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: QNT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,277.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3533件 (Win 974 / Loss 812 / Flat 1747) / skip 5488件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1070 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RARE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.05** / 初期 $100.00 (+20.05%)
- 確定: 3194件 (Win 941 / Loss 1265 / Flat 988) / pending 6件 / skip 3883件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000375 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $120.05

## 6. Latest Market Context

- 更新: 2026-09-26T17:36:44.190204+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=84009.6
- Funnel: target 1070 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +10.54% | $1,010,043.63 |
| LSK/USDT:USDT | +5.02% | $2,465,988.30 |
| QNT/USDT:USDT | +4.99% | $14,724,629.57 |
| GRAM/USDT:USDT | +3.76% | $2,241,292.07 |
| GALA/USDT:USDT | +3.44% | $2,614,343.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PAID/USDT:USDT | below_1h_threshold | +4.72% | +4.79% |
| RARE/USDT:USDT | below_1h_threshold | +3.56% | +3.63% |
| LSK/USDT:USDT | below_1h_threshold | +1.65% | +1.72% |
| KAS/USDT:USDT | below_1h_threshold | +1.59% | +1.66% |
| WLD/USDT:USDT | below_1h_threshold | +1.37% | +1.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
