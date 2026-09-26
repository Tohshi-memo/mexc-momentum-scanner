# Decision Report

- generated_at: 2026-09-26T11:16:35.466380+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15597**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15597, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.57% | **-1.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +2.26% | **+0.79%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.55% | **+0.49%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.53% | **+0.40%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.30% | **+1.81%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.37% | **+1.69%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.68% | **+1.47%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.50% | **+1.22%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.45% | **+1.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.79** / 初期 $100.00 (+20.79%)
- 確定トレード: 223件 (TP 82 / SL 135 / EXP 6)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.79
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,262.51** / 初期 $100.00 (+1162.51%)
- 確定: 5958件 (Win 1760 / Loss 1912 / Flat 2286) / skip 6200件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,262.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$265.91** / 初期 $100.00 (+165.91%)
- 確定: 3527件 (Win 973 / Loss 807 / Flat 1747) / skip 5481件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0678 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $265.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.41** / 初期 $100.00 (+19.41%)
- 確定: 3186件 (Win 937 / Loss 1262 / Flat 987) / pending 0件 / skip 3881件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000361 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $119.41

## 6. Latest Market Context

- 更新: 2026-09-26T11:16:19.999576+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=84132.6
- Funnel: target 1067 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PAID/USDT:USDT | +319.12% | $2,291,676.41 |
| RARE/USDT:USDT | +48.27% | $5,488,983.67 |
| BATON/USDT:USDT | +38.23% | $1,330,546.96 |
| 2Z/USDT:USDT | +31.05% | $3,054,981.93 |
| BR/USDT:USDT | +26.65% | $10,829,053.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +1.56% | +1.56% |
| BR/USDT:USDT | below_1h_threshold | +1.50% | +1.50% |
| 2Z/USDT:USDT | below_1h_threshold | +1.41% | +1.41% |
| RARE/USDT:USDT | below_1h_threshold | +1.18% | +1.18% |
| JTO/USDT:USDT | below_1h_threshold | +1.16% | +1.17% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
