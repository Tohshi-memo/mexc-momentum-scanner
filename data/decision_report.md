# Decision Report

- generated_at: 2026-05-09T07:42:34.905118+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3864**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.28% / filled 20/20。**
- 全期間 MARKET基準: n=3864, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.43% | **+1.43%** |
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.94% | **+0.61%** |
| LIMIT_BB3S | 6/14 | 42.9% | +1.21% | **+0.52%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.50% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.95% | **+0.88%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.27% | **+0.20%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.06% | **-0.04%** |

## 2. $100 Live Portfolio

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定トレード: 29件 (TP 7 / SL 19 / EXP 3)
- 最新: LUNC/USDT:USDT EXPIRED PnL +3.11% 残高後 $98.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 194件 (Win 48 / Loss 64 / Flat 82) / skip 231件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T07:42:31.795310+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=80186.6
- Funnel: target 767 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DYM/USDT:USDT | +34.57% | $2,732,827.85 |
| CORE/USDT:USDT | +23.22% | $2,780,265.48 |
| ZEREBRO/USDT:USDT | +22.74% | $1,446,897.23 |
| REZ/USDT:USDT | +18.55% | $1,752,920.25 |
| ICP/USDT:USDT | +17.37% | $202,689,901.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DYM/USDT:USDT | below_1h_threshold | +3.09% | +3.12% |
| PLAY/USDT:USDT | below_1h_threshold | +2.94% | +2.98% |
| SAHARA/USDT:USDT | below_1h_threshold | +1.75% | +1.78% |
| DEEP/USDT:USDT | below_1h_threshold | +1.47% | +1.50% |
| THETA/USDT:USDT | below_1h_threshold | +1.46% | +1.49% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
