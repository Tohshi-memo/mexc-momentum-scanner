# Decision Report

- generated_at: 2026-09-16T18:11:30.237365+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14726**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14726, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 12/20 | 60.0% | +2.71% | **+1.63%** |
| LIMIT_7PCT | 6/20 | 30.0% | +5.40% | **+1.62%** |
| LIMIT_6PCT | 8/20 | 40.0% | +3.42% | **+1.37%** |
| LIMIT_4PCT | 15/20 | 75.0% | +1.60% | **+1.20%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.93% | **+0.96%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +3.06% | **+1.68%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +3.70% | **+1.11%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.07% | **+1.03%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.50% | **+1.00%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.60% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,165.60** / 初期 $100.00 (+1065.60%)
- 確定: 5599件 (Win 1679 / Loss 1813 / Flat 2107) / skip 5688件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,165.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$240.73** / 初期 $100.00 (+140.73%)
- 確定: 3129件 (Win 870 / Loss 746 / Flat 1513) / skip 5008件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0905 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $240.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2956件 (Win 878 / Loss 1165 / Flat 913) / pending 0件 / skip 3241件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000299 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-16T18:11:17.461475+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.54% price=76080.0
- Funnel: target 1059 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +20.70% | $6,156,895.37 |
| COTI/USDT:USDT | +11.46% | $1,075,033.34 |
| LSK/USDT:USDT | +9.06% | $38,339,751.38 |
| BR/USDT:USDT | +7.49% | $39,326,015.49 |
| ZEC/USDT:USDT | +6.27% | $582,778,133.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_relative_strength | +5.42% | +4.88% |
| DASH/USDT:USDT | below_relative_strength | +5.36% | +4.83% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +4.19% | +3.65% |
| ARB/USDT:USDT | below_1h_threshold | +4.12% | +3.59% |
| UNI/USDT:USDT | below_1h_threshold | +3.83% | +3.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
