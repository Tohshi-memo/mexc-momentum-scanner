# Decision Report

- generated_at: 2026-05-09T08:57:51.725513+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3869**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.73% / filled 20/20。**
- 全期間 MARKET基準: n=3869, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.96% | **+1.96%** |
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.58% | **+0.35%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.09% | **+0.04%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
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
- 確定: 194件 (Win 48 / Loss 64 / Flat 82) / skip 236件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T08:57:48.563885+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=80370.4
- Funnel: target 767 → liquid 178 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.5 >= 65=1, 4h RSI 65.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DYM/USDT:USDT | +31.54% | $3,119,898.79 |
| ZEREBRO/USDT:USDT | +24.29% | $1,744,808.83 |
| ACE/USDT:USDT | +22.83% | $1,101,103.59 |
| PHAROS/USDT:USDT | +20.05% | $17,008,165.12 |
| ICP/USDT:USDT | +17.31% | $189,771,928.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_relative_strength | +5.13% | +4.89% |
| ON/USDT:USDT | below_1h_threshold | +3.36% | +3.13% |
| RAVE/USDT:USDT | below_1h_threshold | +2.94% | +2.71% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.88% | +1.65% |
| BRETT/USDT:USDT | below_1h_threshold | +1.69% | +1.46% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
