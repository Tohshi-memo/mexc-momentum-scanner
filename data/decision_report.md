# Decision Report

- generated_at: 2026-05-09T13:37:39.556971+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3883**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=3883, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.66% | **+0.66%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_BB3S | 4/11 | 36.4% | +0.34% | **+0.12%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/9 | 77.8% | +0.48% | **+0.37%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.48% | **+0.22%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.34% | **+0.12%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.12% | **+0.03%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定トレード: 29件 (TP 7 / SL 19 / EXP 3)
- 最新: LUNC/USDT:USDT EXPIRED PnL +3.11% 残高後 $98.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 194件 (Win 48 / Loss 64 / Flat 82) / skip 250件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T13:37:33.715749+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=80345.8
- Funnel: target 769 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +34.83% | $25,047,263.34 |
| DYM/USDT:USDT | +33.33% | $6,044,059.87 |
| ZEREBRO/USDT:USDT | +31.10% | $3,227,393.99 |
| SAHARA/USDT:USDT | +27.13% | $3,616,257.38 |
| BILL/USDT:USDT | +22.41% | $19,826,189.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +5.00% | +5.03% |
| SIREN/USDT:USDT | below_1h_threshold | +2.77% | +2.80% |
| LIT/USDT:USDT | below_1h_threshold | +2.77% | +2.79% |
| SATO/USDT:USDT | below_1h_threshold | +2.25% | +2.27% |
| BILL/USDT:USDT | below_1h_threshold | +2.08% | +2.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
