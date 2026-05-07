# Decision Report

- generated_at: 2026-05-07T02:52:41.166597+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3537**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3537, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +3.43% | **+1.03%** |
| LIMIT_7PCT | 8/20 | 40.0% | +2.40% | **+0.96%** |
| LIMIT_8PCT | 6/20 | 30.0% | +2.57% | **+0.77%** |
| LIMIT_6PCT | 11/20 | 55.0% | +1.39% | **+0.77%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.74% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +4.66% | **+2.56%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.15% | **+2.52%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| ASK_LONG | 20/20 | 100.0% | +1.79% | **+1.79%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.85% | **+1.66%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$102.63** / 初期 $100.00 (+2.63%)
- 確定: 32件 (Win 11 / Loss 13 / Flat 8) / skip 66件
- 成長率目線: 平均log +0.000813 / 幾何平均 +0.081% per trade / maxDD +2.48%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $102.63

## 4. Latest Market Context

- 更新: 2026-05-07T02:52:37.488602+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=81042.6
- Funnel: target 770 → liquid 188 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.2 >= 65=1, 4h RSI 82.8 >= 65=1, 4h RSI 74.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +215.29% | $1,168,647.67 |
| DOGS/USDT:USDT | +80.46% | $8,150,357.45 |
| FHE/USDT:USDT | +32.30% | $16,306,025.11 |
| PENGUIN/USDT:USDT | +27.58% | $1,155,144.15 |
| TONCOIN/USDT:USDT | +16.15% | $257,782,786.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.26% | +4.35% |
| TONCOIN/USDT:USDT | below_1h_threshold | +4.25% | +4.35% |
| ORCA/USDT:USDT | below_1h_threshold | +3.63% | +3.73% |
| LAB/USDT:USDT | below_1h_threshold | +3.07% | +3.17% |
| TAG/USDT:USDT | below_1h_threshold | +3.01% | +3.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
