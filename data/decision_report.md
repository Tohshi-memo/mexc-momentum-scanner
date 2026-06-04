# Decision Report

- generated_at: 2026-06-04T02:42:51.828528+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5595**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.42% / filled 20/20。**
- 全期間 MARKET基準: n=5595, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+4.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.42% | **+4.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.42% | **+4.42%** |
| ASK | 20/20 | 100.0% | +4.38% | **+4.38%** |
| LIMIT_1PCT | 16/20 | 80.0% | +4.04% | **+3.24%** |
| LIMIT_2PCT | 11/20 | 55.0% | +3.49% | **+1.92%** |
| LIMIT_ATR | 10/20 | 50.0% | +3.34% | **+1.67%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +3.05% | **+1.22%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.53% | **+1.13%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | -0.33% | **-0.20%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -0.63% | **-0.22%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | -0.98% | **-0.64%** |

## 2. $100 Live Portfolio

- 残高: **$99.04** / 初期 $100.00 (-0.96%)
- 確定トレード: 94件 (TP 29 / SL 62 / EXP 3)
- 最新: ICP/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.04
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1005件 (Win 239 / Loss 312 / Flat 454) / skip 1151件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LIT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T02:42:48.519118+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +2.03% price=63402.1
- Funnel: target 771 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +25.77% | $23,573,988.36 |
| STO/USDT:USDT | +16.97% | $6,971,916.95 |
| EPIC/USDT:USDT | +11.16% | $3,638,699.05 |
| MAGMA/USDT:USDT | +10.86% | $4,463,870.26 |
| BP/USDT:USDT | +10.58% | $1,581,528.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +4.68% | +2.65% |
| LIT/USDT:USDT | below_1h_threshold | +3.00% | +0.97% |
| GUA/USDT:USDT | below_1h_threshold | +2.86% | +0.83% |
| EPIC/USDT:USDT | below_1h_threshold | +2.70% | +0.67% |
| WLD/USDT:USDT | below_1h_threshold | +2.51% | +0.48% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
