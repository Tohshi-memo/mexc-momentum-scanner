# Decision Report

- generated_at: 2026-09-26T13:16:25.765754+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15601**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15601, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.68% | **-0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +0.53% | **+0.43%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.00% | **+0.35%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.37% | **+0.34%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.16% | **+1.87%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.57% | **+1.67%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +4.06% | **+1.62%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.62% | **+1.31%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.92% | **+1.05%** |

## 2. $100 Live Portfolio

- 残高: **$120.87** / 初期 $100.00 (+20.87%)
- 確定トレード: 224件 (TP 82 / SL 135 / EXP 7)
- 最新: UNI/USDT:USDT EXPIRED PnL +1.69% 残高後 $120.87
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,262.62** / 初期 $100.00 (+1162.62%)
- 確定: 5962件 (Win 1762 / Loss 1914 / Flat 2286) / skip 6200件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,262.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$264.94** / 初期 $100.00 (+164.94%)
- 確定: 3531件 (Win 974 / Loss 810 / Flat 1747) / skip 5481件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0978 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $264.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.41** / 初期 $100.00 (+19.41%)
- 確定: 3186件 (Win 937 / Loss 1262 / Flat 987) / pending 0件 / skip 3882件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000372 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $119.41

## 6. Latest Market Context

- 更新: 2026-09-26T13:16:16.810721+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=83955.6
- Funnel: target 1070 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PAID/USDT:USDT | +289.58% | $2,636,191.06 |
| RARE/USDT:USDT | +39.39% | $6,704,704.92 |
| BATON/USDT:USDT | +31.64% | $1,255,636.80 |
| BR/USDT:USDT | +26.87% | $10,426,278.72 |
| 2Z/USDT:USDT | +23.93% | $3,414,659.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUBARAK/USDT:USDT | below_1h_threshold | +4.78% | +4.85% |
| RARE/USDT:USDT | below_1h_threshold | +1.30% | +1.37% |
| PYTH/USDT:USDT | below_1h_threshold | +0.98% | +1.06% |
| BEAT/USDT:USDT | below_1h_threshold | +0.96% | +1.03% |
| QNT/USDT:USDT | below_1h_threshold | +0.69% | +0.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
