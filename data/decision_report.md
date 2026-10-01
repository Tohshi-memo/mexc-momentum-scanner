# Decision Report

- generated_at: 2026-10-01T11:01:33.060640+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15897**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15897, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.68% | **-1.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +0.95% | **+0.52%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +0.56% | **+0.06%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.05% | **+0.04%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.03% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.22% | **+2.00%** |
| LIMIT_BB3S_LONG | 8/10 | 80.0% | +2.41% | **+1.92%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.55% | **+1.66%** |
| MARKET_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.56% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,287.88** / 初期 $100.00 (+1187.88%)
- 確定: 6015件 (Win 1781 / Loss 1935 / Flat 2299) / skip 6443件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,287.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$269.14** / 初期 $100.00 (+169.14%)
- 確定: 3550件 (Win 982 / Loss 816 / Flat 1752) / skip 5758件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1252 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $269.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4057件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000283 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T11:01:22.242688+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=83866.6
- Funnel: target 1097 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +70.00% | $17,045,764.39 |
| LONGXIA/USDT:USDT | +43.02% | $3,177,192.61 |
| NOM/USDT:USDT | +25.96% | $2,537,653.45 |
| NIGHT/USDT:USDT | +21.59% | $8,453,651.70 |
| CT/USDT:USDT | +20.95% | $6,305,435.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +1.47% | +1.54% |
| SNXX/USDT:USDT | below_1h_threshold | +1.34% | +1.42% |
| MOVR/USDT:USDT | below_1h_threshold | +1.14% | +1.22% |
| SOXL/USDT:USDT | below_1h_threshold | +0.79% | +0.87% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.75% | +0.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
