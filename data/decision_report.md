# Decision Report

- generated_at: 2026-05-09T10:52:58.398701+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3879**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=3879, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |
| ASK | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_BB3S | 5/13 | 38.5% | +1.22% | **+0.47%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.12% | **+0.09%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +1.84% | **+1.31%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.30% | **+0.52%** |
| ASK_LONG | 20/20 | 100.0% | +0.23% | **+0.23%** |
| MARKET_LONG | 20/20 | 100.0% | +0.21% | **+0.21%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.22% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定トレード: 29件 (TP 7 / SL 19 / EXP 3)
- 最新: LUNC/USDT:USDT EXPIRED PnL +3.11% 残高後 $98.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 194件 (Win 48 / Loss 64 / Flat 82) / skip 246件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T10:52:52.368544+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=80236.1
- Funnel: target 769 → liquid 180 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.2 >= 65=1, 4h RSI 88.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +53.02% | $20,648,408.70 |
| DYM/USDT:USDT | +47.26% | $3,978,643.13 |
| ZEREBRO/USDT:USDT | +33.36% | $2,299,992.26 |
| SAHARA/USDT:USDT | +27.47% | $2,417,775.32 |
| CORE/USDT:USDT | +16.74% | $3,262,426.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANTHROPIC/USDT:USDT | below_1h_threshold | +4.75% | +4.70% |
| ON/USDT:USDT | below_1h_threshold | +4.64% | +4.59% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +4.31% | +4.26% |
| SAGA/USDT:USDT | below_1h_threshold | +3.41% | +3.36% |
| JASMY/USDT:USDT | below_1h_threshold | +3.26% | +3.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
