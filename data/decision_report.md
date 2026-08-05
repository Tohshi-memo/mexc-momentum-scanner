# Decision Report

- generated_at: 2026-08-05T05:51:38.428197+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10369**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.23% / filled 20/20。**
- 全期間 MARKET基準: n=10369, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +3.56% | **+3.12%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.55% | **+1.40%** |
| MARKET_LONG | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.34% | **+0.87%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.15% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$623.79** / 初期 $100.00 (+523.79%)
- 確定: 3763件 (Win 1195 / Loss 1230 / Flat 1338) / skip 3167件
- 成長率目線: 平均log +0.000486 / 幾何平均 +0.049% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $623.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.80** / 初期 $100.00 (+44.80%)
- 確定: 1303件 (Win 368 / Loss 303 / Flat 632) / skip 2477件
- 成長率目線: 平均log +0.000284 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1133 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $144.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.42** / 初期 $100.00 (+19.42%)
- 確定: 1119件 (Win 361 / Loss 430 / Flat 328) / pending 6件 / skip 720件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000393 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.42

## 6. Latest Market Context

- 更新: 2026-08-05T05:51:27.248980+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=64290.0
- Funnel: target 939 → liquid 185 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.1 >= 65=1, 4h RSI 82.9 >= 65=1, 4h RSI 68.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +94.12% | $11,559,579.82 |
| HFT/USDT:USDT | +57.94% | $1,462,661.05 |
| BLESS/USDT:USDT | +53.12% | $25,401,579.08 |
| BICO/USDT:USDT | +43.96% | $15,946,672.01 |
| TAKE/USDT:USDT | +35.33% | $1,619,039.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.87% | +3.64% |
| TUT/USDT:USDT | below_1h_threshold | +2.77% | +2.54% |
| VELVET/USDT:USDT | below_1h_threshold | +2.56% | +2.33% |
| HEI/USDT:USDT | below_1h_threshold | +2.50% | +2.27% |
| SNXX/USDT:USDT | below_1h_threshold | +2.20% | +1.97% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
