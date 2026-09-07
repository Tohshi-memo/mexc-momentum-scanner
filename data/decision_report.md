# Decision Report

- generated_at: 2026-09-07T07:31:23.063126+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13868**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.07% / filled 20/20。**
- 全期間 MARKET基準: n=13868, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.58% | **+0.78%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.01% | **+0.45%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.59% | **+0.56%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.59% | **+0.48%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.37% | **+0.26%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.27% | **+0.19%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.60% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$844.96** / 初期 $100.00 (+744.96%)
- 確定: 5141件 (Win 1540 / Loss 1680 / Flat 1921) / skip 5288件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $844.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.18** / 初期 $100.00 (+88.18%)
- 確定: 2571件 (Win 717 / Loss 618 / Flat 1236) / skip 4708件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0726 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $188.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.41** / 初期 $100.00 (+19.41%)
- 確定: 2460件 (Win 730 / Loss 935 / Flat 795) / pending 3件 / skip 2875件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000287 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MEMEROBINHOOD/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $119.41

## 6. Latest Market Context

- 更新: 2026-09-07T07:31:10.279221+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=79421.6
- Funnel: target 1059 → liquid 140 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | +257.14% | $1,412,167.27 |
| BONER/USDT:USDT | +123.64% | $5,141,200.86 |
| XAN/USDT:USDT | +13.78% | $2,300,124.86 |
| ICP/USDT:USDT | +12.44% | $9,638,562.67 |
| BULLA/USDT:USDT | +12.12% | $7,032,359.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +3.99% | +4.23% |
| ICP/USDT:USDT | below_1h_threshold | +2.42% | +2.66% |
| ATOM/USDT:USDT | below_1h_threshold | +1.12% | +1.37% |
| WLD/USDT:USDT | below_1h_threshold | +1.07% | +1.32% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.79% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
