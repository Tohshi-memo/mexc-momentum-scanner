# Decision Report

- generated_at: 2026-05-08T10:02:57.372448+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3767**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.94% / filled 20/20。**
- 全期間 MARKET基準: n=3767, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+1.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.94% | **+1.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.94% | **+1.94%** |
| ASK | 20/20 | 100.0% | +1.84% | **+1.84%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.61% | **+1.45%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.46% | **+0.32%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.52% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.19% | **+0.15%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.21% | **+0.14%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | -0.06% | **-0.05%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | -0.94% | **-0.24%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 26件 (TP 7 / SL 17 / EXP 2)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 191件 (Win 48 / Loss 64 / Flat 79) / skip 137件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T10:02:54.645861+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=79918.9
- Funnel: target 772 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +40.80% | $8,087,619.76 |
| PLAY/USDT:USDT | +39.25% | $8,361,506.92 |
| PHAROS/USDT:USDT | +35.54% | $5,909,764.06 |
| STRK/USDT:USDT | +30.29% | $16,430,739.20 |
| AGT/USDT:USDT | +23.27% | $5,423,818.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +1.94% | +1.83% |
| PLAY/USDT:USDT | below_1h_threshold | +1.43% | +1.32% |
| LAB/USDT:USDT | below_1h_threshold | +1.21% | +1.09% |
| W/USDT:USDT | below_1h_threshold | +1.14% | +1.02% |
| STRK/USDT:USDT | below_1h_threshold | +1.08% | +0.97% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
