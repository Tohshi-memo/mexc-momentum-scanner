# Decision Report

- generated_at: 2026-06-29T19:46:07.856381+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7833**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.14% / filled 20/20。**
- 全期間 MARKET基準: n=7833, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.14% | **+1.14%** |
| ASK | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.78% | **+0.27%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.30% | **+0.18%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.10% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +0.80% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |
| ASK_LONG | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$101.63** / 初期 $100.00 (+1.63%)
- 確定トレード: 43件 (TP 15 / SL 27 / EXP 1)
- 最新: HEI/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.63
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$265.73** / 初期 $100.00 (+165.73%)
- 確定: 2337件 (Win 711 / Loss 777 / Flat 849) / skip 2057件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $265.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 787件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0265 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T19:45:59.212106+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=60446.0
- Funnel: target 811 → liquid 153 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +21.80% | $13,019,779.48 |
| H/USDT:USDT | +10.56% | $5,902,519.58 |
| MYX/USDT:USDT | +9.04% | $2,730,342.66 |
| BAS/USDT:USDT | +8.92% | $2,156,922.28 |
| UB/USDT:USDT | +8.44% | $3,269,142.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +2.95% | +2.67% |
| UB/USDT:USDT | below_1h_threshold | +1.99% | +1.71% |
| BAS/USDT:USDT | below_1h_threshold | +1.97% | +1.69% |
| XPL/USDT:USDT | below_1h_threshold | +1.83% | +1.54% |
| HYPE/USDT:USDT | below_1h_threshold | +1.53% | +1.25% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
