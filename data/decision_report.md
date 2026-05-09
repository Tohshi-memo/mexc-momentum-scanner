# Decision Report

- generated_at: 2026-05-09T10:05:02.080983+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3875**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.28% / filled 20/20。**
- 全期間 MARKET基準: n=3875, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.37% | **+1.37%** |
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |
| LIMIT_BB3S | 6/15 | 40.0% | +0.57% | **+0.23%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.04% | **+0.03%** |
| LIMIT_2PCT | 14/20 | 70.0% | -0.07% | **-0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.41% | **+0.35%** |
| ASK_LONG | 20/20 | 100.0% | +0.21% | **+0.21%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.16% | **+0.06%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.08% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定トレード: 29件 (TP 7 / SL 19 / EXP 3)
- 最新: LUNC/USDT:USDT EXPIRED PnL +3.11% 残高後 $98.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 194件 (Win 48 / Loss 64 / Flat 82) / skip 242件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T10:04:58.618675+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=80179.7
- Funnel: target 769 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +44.87% | $16,203,547.76 |
| DYM/USDT:USDT | +37.21% | $3,520,297.32 |
| ZEREBRO/USDT:USDT | +28.97% | $2,035,028.17 |
| PHAROS/USDT:USDT | +21.42% | $12,398,711.88 |
| SAHARA/USDT:USDT | +18.66% | $1,918,379.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DYM/USDT:USDT | below_1h_threshold | +1.60% | +1.63% |
| SIREN/USDT:USDT | below_1h_threshold | +1.20% | +1.22% |
| PHAROS/USDT:USDT | below_1h_threshold | +1.03% | +1.06% |
| SAHARA/USDT:USDT | below_1h_threshold | +0.98% | +1.01% |
| AGT/USDT:USDT | below_1h_threshold | +0.96% | +0.98% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
