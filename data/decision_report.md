# Decision Report

- generated_at: 2026-09-26T05:51:24.636965+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15571**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15571, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.46% | **-1.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.36% | **+0.88%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.95% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.29% | **+2.46%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.36% | **+2.13%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.04% | **+1.52%** |
| MARKET_LONG | 20/20 | 100.0% | +1.46% | **+1.46%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$120.79** / 初期 $100.00 (+20.79%)
- 確定トレード: 223件 (TP 82 / SL 135 / EXP 6)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.79
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,248.10** / 初期 $100.00 (+1148.10%)
- 確定: 5932件 (Win 1751 / Loss 1901 / Flat 2280) / skip 6200件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PAID/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,248.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$259.61** / 初期 $100.00 (+159.61%)
- 確定: 3501件 (Win 961 / Loss 797 / Flat 1743) / skip 5481件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1286 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PAID/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $259.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.41** / 初期 $100.00 (+19.41%)
- 確定: 3185件 (Win 937 / Loss 1262 / Flat 986) / pending 1件 / skip 3857件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000430 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LDO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.03% 残高後 $119.41

## 6. Latest Market Context

- 更新: 2026-09-26T05:51:13.517253+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=83944.6
- Funnel: target 1067 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PAID/USDT:USDT | +306.62% | $1,111,903.30 |
| BATON/USDT:USDT | +37.88% | $1,535,060.63 |
| PHA/USDT:USDT | +20.58% | $29,696,672.53 |
| ARK/USDT:USDT | +18.89% | $3,470,680.85 |
| H/USDT:USDT | +14.81% | $1,210,634.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BATON/USDT:USDT | below_1h_threshold | +5.00% | +5.00% |
| PHA/USDT:USDT | below_1h_threshold | +4.60% | +4.60% |
| PAID/USDT:USDT | below_1h_threshold | +2.59% | +2.59% |
| GRASS/USDT:USDT | below_1h_threshold | +2.19% | +2.19% |
| CC/USDT:USDT | below_1h_threshold | +1.84% | +1.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
