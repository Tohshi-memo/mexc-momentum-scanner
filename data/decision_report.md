# Decision Report

- generated_at: 2026-09-26T11:36:19.869290+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15599**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15599, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.97% | **-0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +1.70% | **+0.93%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.48% | **+0.74%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.64% | **+0.54%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.10% | **+2.01%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.92% | **+1.31%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.33% | **+1.16%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.80% | **+1.12%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.89% | **+0.94%** |

## 2. $100 Live Portfolio

- 残高: **$120.79** / 初期 $100.00 (+20.79%)
- 確定トレード: 223件 (TP 82 / SL 135 / EXP 6)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.79
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,268.76** / 初期 $100.00 (+1168.76%)
- 確定: 5960件 (Win 1761 / Loss 1913 / Flat 2286) / skip 6200件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 2Z/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,268.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$266.80** / 初期 $100.00 (+166.80%)
- 確定: 3529件 (Win 974 / Loss 808 / Flat 1747) / skip 5481件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0891 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 2Z/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $266.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.41** / 初期 $100.00 (+19.41%)
- 確定: 3186件 (Win 937 / Loss 1262 / Flat 987) / pending 0件 / skip 3882件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000416 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $119.41

## 6. Latest Market Context

- 更新: 2026-09-26T11:36:09.275684+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=84130.4
- Funnel: target 1067 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PAID/USDT:USDT | +309.18% | $2,359,551.07 |
| RARE/USDT:USDT | +42.23% | $5,818,030.17 |
| BATON/USDT:USDT | +35.11% | $1,347,094.03 |
| 2Z/USDT:USDT | +25.94% | $3,173,388.82 |
| BR/USDT:USDT | +25.60% | $11,081,466.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RUNE/USDT:USDT | below_1h_threshold | +2.17% | +2.18% |
| PYTH/USDT:USDT | below_1h_threshold | +1.85% | +1.86% |
| DASH/USDT:USDT | below_1h_threshold | +1.77% | +1.78% |
| BEAT/USDT:USDT | below_1h_threshold | +1.66% | +1.66% |
| SPX/USDT:USDT | below_1h_threshold | +1.56% | +1.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
