# Decision Report

- generated_at: 2026-06-11T14:47:17.501103+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6360**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6360, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.08% | **+0.05%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.80% | **+1.08%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.28% | **+1.02%** |
| ASK_LONG | 20/20 | 100.0% | +0.76% | **+0.76%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.37% | **+0.55%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.91** / 初期 $100.00 (+48.91%)
- 確定: 1280件 (Win 324 / Loss 405 / Flat 551) / skip 1641件
- 成長率目線: 平均log +0.000311 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $148.91

## 4. Latest Market Context

- 更新: 2026-06-11T14:47:10.910837+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=62842.7
- Funnel: target 782 → liquid 154 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.2 >= 65=1, 4h RSI 67.4 >= 65=1, 4h RSI 74.8 >= 65=1, 4h RSI 74.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +104.45% | $86,693,029.79 |
| H/USDT:USDT | +96.32% | $28,569,199.32 |
| AIO/USDT:USDT | +68.11% | $8,991,114.92 |
| BEAT/USDT:USDT | +63.96% | $246,358,007.83 |
| COLLECT/USDT:USDT | +53.11% | $2,381,895.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRV/USDT:USDT | below_1h_threshold | +4.52% | +4.83% |
| LAB/USDT:USDT | below_1h_threshold | +4.08% | +4.39% |
| PYTH/USDT:USDT | below_1h_threshold | +3.85% | +4.16% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.55% | +2.86% |
| A/USDT:USDT | below_1h_threshold | +2.23% | +2.53% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
