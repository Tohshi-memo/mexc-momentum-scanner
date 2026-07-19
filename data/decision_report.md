# Decision Report

- generated_at: 2026-07-19T17:51:26.185123+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9062**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.41% / filled 20/20。**
- 全期間 MARKET基準: n=9062, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.50% | **+0.35%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +3.70% | **+1.11%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.05% | **+1.03%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| MARKET_LONG | 20/20 | 100.0% | +0.18% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$109.69** / 初期 $100.00 (+9.69%)
- 確定トレード: 119件 (TP 43 / SL 71 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -3.31% 残高後 $109.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$401.25** / 初期 $100.00 (+301.25%)
- 確定: 3124件 (Win 982 / Loss 999 / Flat 1143) / skip 2499件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $401.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$125.55** / 初期 $100.00 (+25.55%)
- 確定: 1023件 (Win 264 / Loss 218 / Flat 541) / skip 1450件
- 成長率目線: 平均log +0.000222 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0582 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $125.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定: 262件 (Win 91 / Loss 130 / Flat 41) / pending 5件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000234 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $100.97

## 6. Latest Market Context

- 更新: 2026-07-19T17:51:16.970337+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=64561.6
- Funnel: target 885 → liquid 128 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.4 >= 65=1, 4h RSI 80.9 >= 65=1, 4h RSI 74.4 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +29.30% | $61,030,290.06 |
| ESPORTS/USDT:USDT | +14.74% | $64,739,215.55 |
| B/USDT:USDT | +10.60% | $36,204,767.23 |
| DEXE/USDT:USDT | +9.15% | $1,498,291.69 |
| TLM/USDT:USDT | +7.95% | $12,165,387.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.30% | +4.23% |
| DEXE/USDT:USDT | below_1h_threshold | +2.80% | +2.72% |
| ALLO/USDT:USDT | below_1h_threshold | +2.14% | +2.06% |
| SYN/USDT:USDT | below_1h_threshold | +1.61% | +1.53% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.44% | +1.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
