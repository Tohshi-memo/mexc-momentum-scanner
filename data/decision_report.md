# Decision Report

- generated_at: 2026-05-09T09:27:32.291567+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3870**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.33% / filled 20/20。**
- 全期間 MARKET基準: n=3870, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+2.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.33% | **+2.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.53% | **+2.53%** |
| MARKET | 20/20 | 100.0% | +2.33% | **+2.33%** |
| LIMIT_BB3S | 5/15 | 33.3% | +1.48% | **+0.49%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.58% | **+0.35%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.58% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.04% | **-0.02%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.98% | **-0.10%** |
| MARKET_LONG | 20/20 | 100.0% | -0.35% | **-0.35%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.74% | **-0.63%** |

## 2. $100 Live Portfolio

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定トレード: 29件 (TP 7 / SL 19 / EXP 3)
- 最新: LUNC/USDT:USDT EXPIRED PnL +3.11% 残高後 $98.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 194件 (Win 48 / Loss 64 / Flat 82) / skip 237件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T09:27:28.989884+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=80224.1
- Funnel: target 769 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DYM/USDT:USDT | +33.18% | $3,299,549.89 |
| ZEREBRO/USDT:USDT | +26.30% | $1,917,456.58 |
| PHAROS/USDT:USDT | +22.14% | $17,467,858.49 |
| ACE/USDT:USDT | +20.11% | $1,494,241.66 |
| SAHARA/USDT:USDT | +17.13% | $1,717,498.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.00% | +3.19% |
| RAVE/USDT:USDT | below_1h_threshold | +2.30% | +2.49% |
| SAHARA/USDT:USDT | below_1h_threshold | +2.23% | +2.42% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.93% | +2.13% |
| SATO/USDT:USDT | below_1h_threshold | +1.77% | +1.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
