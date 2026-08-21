# Decision Report

- generated_at: 2026-08-21T10:51:36.013491+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12183**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.19% / filled 20/20。**
- 全期間 MARKET基準: n=12183, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.19% | **+1.19%** |
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/10 | 80.0% | +5.60% | **+4.48%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.75% | **+1.24%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.04% | **+0.84%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$640.35** / 初期 $100.00 (+540.35%)
- 確定: 4361件 (Win 1337 / Loss 1434 / Flat 1590) / skip 4383件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $640.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1823件 (Win 502 / Loss 429 / Flat 892) / skip 3771件
- 成長率目線: 平均log +0.000237 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0588 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.00** / 初期 $100.00 (+17.00%)
- 確定: 1823件 (Win 540 / Loss 692 / Flat 591) / pending 1件 / skip 1834件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000161 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CHIP/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.00

## 6. Latest Market Context

- 更新: 2026-08-21T10:51:22.186649+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=77759.1
- Funnel: target 1018 → liquid 204 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.9 >= 65=2, 4h RSI 85.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +111.66% | $6,968,569.42 |
| ENA/USDT:USDT | +36.54% | $119,565,406.41 |
| BB/USDT:USDT | +32.23% | $4,691,178.70 |
| NEIROCTO/USDT:USDT | +24.69% | $4,101,215.36 |
| BTW/USDT:USDT | +22.61% | $76,229,950.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +4.92% | +5.10% |
| BERA/USDT:USDT | below_1h_threshold | +4.47% | +4.66% |
| USELESS/USDT:USDT | below_1h_threshold | +4.35% | +4.53% |
| PENGU/USDT:USDT | below_1h_threshold | +3.52% | +3.70% |
| GALA/USDT:USDT | below_1h_threshold | +3.47% | +3.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
