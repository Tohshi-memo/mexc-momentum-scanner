# Decision Report

- generated_at: 2026-08-05T01:51:46.157311+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10338**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10338, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.45% | **-0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.59% | **+0.69%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.37% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +2.00% | **+2.00%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.74% | **+0.52%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.92% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$580.68** / 初期 $100.00 (+480.68%)
- 確定: 3735件 (Win 1181 / Loss 1223 / Flat 1331) / skip 3164件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $580.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1285件 (Win 359 / Loss 299 / Flat 627) / skip 2464件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0048 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.49** / 初期 $100.00 (+17.49%)
- 確定: 1094件 (Win 351 / Loss 423 / Flat 320) / pending 5件 / skip 715件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000282 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.49

## 6. Latest Market Context

- 更新: 2026-08-05T01:51:31.250667+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.42% price=64240.0
- Funnel: target 937 → liquid 181 → pre 50 → checked 50 → surge 6 → strict 1
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.8 >= 65=1, 4h RSI 73.2 >= 65=1, 4h RSI 84.7 >= 65=1, 4h RSI 75.9 >= 65=1, 4h RSI 76.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +63.09% | $5,228,716.64 |
| MARSCOIN/USDT:USDT | +34.33% | $1,073,241.04 |
| CASHCAT/USDT:USDT | +30.76% | $1,142,309.49 |
| TAKE/USDT:USDT | +29.32% | $1,369,944.18 |
| SKYAI/USDT:USDT | +23.62% | $50,104,767.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ADVANTESTSTOCK/USDT:USDT | below_1h_threshold | +4.83% | +4.41% |
| BLESS/USDT:USDT | below_1h_threshold | +4.14% | +3.72% |
| ALABSTOCK/USDT:USDT | below_1h_threshold | +3.41% | +2.99% |
| LIT/USDT:USDT | below_1h_threshold | +3.05% | +2.63% |
| BEAT/USDT:USDT | below_1h_threshold | +2.80% | +2.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
