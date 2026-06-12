# Decision Report

- generated_at: 2026-06-12T17:48:59.189213+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6529**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.16% / filled 20/20。**
- 全期間 MARKET基準: n=6529, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +2.16% | **+1.19%** |
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |
| ASK | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.41% | **+1.53%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.92% | **+0.69%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.30% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$94.22** / 初期 $100.00 (-5.78%)
- 確定トレード: 22件 (TP 3 / SL 18 / EXP 1)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $94.22
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$166.31** / 初期 $100.00 (+66.31%)
- 確定: 1402件 (Win 387 / Loss 457 / Flat 558) / skip 1688件
- 成長率目線: 平均log +0.000363 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $166.31

## 4. Latest Market Context

- 更新: 2026-06-12T17:48:54.037262+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=63821.1
- Funnel: target 774 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +14.13% | $8,986,906.41 |
| AIN/USDT:USDT | +12.73% | $1,632,182.15 |
| ESPORTS/USDT:USDT | +9.49% | $67,391,622.41 |
| H/USDT:USDT | +8.99% | $29,890,048.94 |
| SPCXSTOCK/USDT:USDT | +7.00% | $207,507,879.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +4.36% | +4.57% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.98% | +4.18% |
| HOME/USDT:USDT | below_1h_threshold | +3.17% | +3.37% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.78% | +2.98% |
| ENJ/USDT:USDT | below_1h_threshold | +2.57% | +2.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
