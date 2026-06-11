# Decision Report

- generated_at: 2026-06-11T13:05:49.123483+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6352**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6352, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.20% | **+0.07%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_BB3S | 7/19 | 36.8% | -0.10% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.43% | **+1.82%** |
| ASK_LONG | 20/20 | 100.0% | +1.67% | **+1.67%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.69% | **+0.93%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$149.67** / 初期 $100.00 (+49.67%)
- 確定: 1273件 (Win 321 / Loss 401 / Flat 551) / skip 1640件
- 成長率目線: 平均log +0.000317 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $149.67

## 4. Latest Market Context

- 更新: 2026-06-11T13:05:43.202806+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=62900.0
- Funnel: target 782 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +103.50% | $21,429,776.95 |
| VELVET/USDT:USDT | +75.44% | $82,537,103.96 |
| BEAT/USDT:USDT | +55.40% | $227,020,123.63 |
| COLLECT/USDT:USDT | +47.78% | $2,254,233.59 |
| AIO/USDT:USDT | +47.64% | $8,601,310.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +2.74% | +2.86% |
| STG/USDT:USDT | below_1h_threshold | +1.88% | +2.00% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.49% | +1.61% |
| H/USDT:USDT | below_1h_threshold | +1.44% | +1.56% |
| FHE/USDT:USDT | below_1h_threshold | +1.01% | +1.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
