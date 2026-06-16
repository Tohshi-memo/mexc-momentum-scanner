# Decision Report

- generated_at: 2026-06-16T20:55:51.075784+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6886**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6886, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.14% | **+0.45%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.23% | **+0.17%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.96% | **+0.14%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.15% | **+0.14%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.52% | **+1.14%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.64% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.49% | **+0.49%** |
| ASK_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.37% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$185.43** / 初期 $100.00 (+85.43%)
- 確定: 1759件 (Win 465 / Loss 553 / Flat 741) / skip 1688件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $185.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.68** / 初期 $100.00 (-2.32%)
- 確定: 160件 (Win 29 / Loss 31 / Flat 100) / skip 137件
- 成長率目線: 平均log -0.000147 / 幾何平均 -0.015% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0294 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $97.68

## 5. Latest Market Context

- 更新: 2026-06-16T20:55:44.472516+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=65821.3
- Funnel: target 782 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +17.26% | $28,577,298.11 |
| PLAY/USDT:USDT | +16.21% | $1,633,034.44 |
| BLESS/USDT:USDT | +14.59% | $1,733,797.18 |
| ESPORTS/USDT:USDT | +12.87% | $1,745,619.72 |
| UNI/USDT:USDT | +8.93% | $41,611,172.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.77% | +3.51% |
| WLD/USDT:USDT | below_1h_threshold | +3.58% | +3.33% |
| PLAY/USDT:USDT | below_1h_threshold | +3.46% | +3.20% |
| UAI/USDT:USDT | below_1h_threshold | +3.21% | +2.95% |
| UNI/USDT:USDT | below_1h_threshold | +3.04% | +2.78% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
