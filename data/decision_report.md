# Decision Report

- generated_at: 2026-06-26T14:42:23.406271+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7635**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.33% / filled 20/20。**
- 全期間 MARKET基準: n=7635, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.33% | **+0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 2/13 | 15.4% | +3.43% | **+0.53%** |
| MARKET | 20/20 | 100.0% | +0.33% | **+0.33%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.21% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.85% | **+0.85%** |
| ASK_LONG | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | -0.37% | **-0.24%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.23** / 初期 $100.00 (+130.23%)
- 確定: 2160件 (Win 639 / Loss 715 / Flat 806) / skip 2036件
- 成長率目線: 平均log +0.000386 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $230.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 382件 (Win 103 / Loss 100 / Flat 179) / skip 664件
- 成長率目線: 平均log +0.000192 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-26T14:42:16.408148+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.91% price=59596.4
- Funnel: target 806 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +65.88% | $6,626,830.12 |
| ICNT/USDT:USDT | +45.69% | $3,138,265.49 |
| AGLD/USDT:USDT | +38.64% | $1,146,436.63 |
| VELVET/USDT:USDT | +28.96% | $9,226,806.04 |
| BEAT/USDT:USDT | +20.46% | $49,581,237.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGLD/USDT:USDT | below_1h_threshold | +4.50% | +5.41% |
| ICNT/USDT:USDT | below_1h_threshold | +3.87% | +4.79% |
| BLESS/USDT:USDT | below_1h_threshold | +3.20% | +4.12% |
| JTO/USDT:USDT | below_1h_threshold | +2.74% | +3.66% |
| ALLO/USDT:USDT | below_1h_threshold | +2.62% | +3.53% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
