# Decision Report

- generated_at: 2026-07-01T20:26:48.260055+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8012**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=8012, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +3.09% | **+0.77%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.91% | **+0.69%** |
| LIMIT_7PCT | 7/20 | 35.0% | +1.66% | **+0.58%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.23% | **+0.49%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.77% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| ASK_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.51% | **+0.36%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.36% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$275.09** / 初期 $100.00 (+175.09%)
- 確定: 2409件 (Win 737 / Loss 798 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LIT/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $275.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.58** / 初期 $100.00 (+7.58%)
- 確定: 529件 (Win 135 / Loss 124 / Flat 270) / skip 894件
- 成長率目線: 平均log +0.000138 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0425 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LIT/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $107.58

## 5. Latest Market Context

- 更新: 2026-07-01T20:26:44.148828+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=59965.3
- Funnel: target 825 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +65.00% | $1,363,094.87 |
| LIT/USDT:USDT | +14.20% | $5,229,585.64 |
| RIF/USDT:USDT | +10.35% | $2,789,035.67 |
| NOM/USDT:USDT | +8.97% | $4,731,870.86 |
| VELVET/USDT:USDT | +6.99% | $26,876,211.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| M/USDT:USDT | below_1h_threshold | +3.75% | +3.81% |
| BEAT/USDT:USDT | below_1h_threshold | +3.08% | +3.14% |
| BASED/USDT:USDT | below_1h_threshold | +2.93% | +2.99% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.58% | +2.64% |
| LIT/USDT:USDT | below_1h_threshold | +1.66% | +1.72% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
